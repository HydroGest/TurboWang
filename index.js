const fs = require('fs');
const path = require('path');
// You should use require('@turbowarp/packager') instead
// We use a strange require() in this demo because we use this to test the API internally
const Packager = require('@turbowarp/packager');

const run = async (projectName) => {
  const projectData = fs.readFileSync(path.join(__dirname, '', projectName,'/project.sb3.zip'));

  const loadedProject = await Packager.loadProject(projectData);

  const packager = new Packager.Packager();
  //packager.options.turbo = true;
  packager.options.highQualityPen = true;
  packager.options.loadingScreen.text = 'TurboWang 加载中......'
  packager.options.controls.greenFlag.enabled = true;
  packager.options.controls.stopAll.enabled = true;
  packager.options.controls.fullscreen.enabled = true;
  packager.options.controls.pause.enabled = true;
  packager.options.maxclone = 114514;
 
  
  
  
  packager.project = loadedProject;

  const result = await packager.package();
  console.log(result.data)
  fs.writeFileSync(path.join(__dirname, projectName,'/output.html'), result.data);
};
var projectName = process.argv[2];
run(projectName)
  .catch((err) => {
    console.error(err);
    process.exit(1);
  });
