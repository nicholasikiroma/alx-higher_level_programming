const characterDiv = $('DIV#character');
const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.getJSON(URL, function (data) {
    const characterName = data.name;
    characterDiv.text(characterName);
});
