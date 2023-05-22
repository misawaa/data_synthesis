const info = [
    {
      name: 'echo',
      description: 'Repeat what you said',
    },
];
async function cmd(interaction) {

    const input = interaction.options.getString('input');

    await interaction.reply(`You just said: ${input}`);
}

module.exports = {
    info: info,
    exec: cmd
}