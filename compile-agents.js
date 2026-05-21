import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const agentsDir = path.join(__dirname, 'agents');
const outputFile = path.join(__dirname, 'src', 'agents-data.json');

try {
    const files = fs.readdirSync(agentsDir).filter(file => file.endsWith('.md'));
    const agents = [];

    files.forEach(file => {
        const filePath = path.join(agentsDir, file);
        const content = fs.readFileSync(filePath, 'utf-8');
        
        // Split by ---
        const parts = content.split('---');
        if (parts.length >= 3) {
            const frontmatterText = parts[1];
            const bodyText = parts.slice(2).join('---').trim();
            
            const frontmatter = {};
            frontmatterText.split('\n').forEach(line => {
                const colonIndex = line.indexOf(':');
                if (colonIndex !== -1) {
                    const key = line.substring(0, colonIndex).trim();
                    const value = line.substring(colonIndex + 1).trim();
                    frontmatter[key] = value;
                }
            });
            
            const id = file.replace('.md', '');
            
            agents.push({
                id: id,
                name: frontmatter.name || id.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '),
                description: frontmatter.description || '',
                tools: frontmatter.tools ? frontmatter.tools.split(',').map(t => t.trim()) : [],
                model: frontmatter.model || 'inherit',
                skills: frontmatter.skills ? frontmatter.skills.split(',').map(s => s.trim()) : [],
                body: bodyText
            });
        }
    });

    fs.writeFileSync(outputFile, JSON.stringify(agents, null, 2), 'utf-8');
    console.log(`Successfully compiled ${agents.length} agents into src/agents-data.json`);
} catch (error) {
    console.error('Error compiling agents:', error);
    process.exit(1);
}
