type ID = number | string;
type DS = number | string;

interface Package {
  Size: number;
  DataType: DS;
  PackageIdentifier: ID;
}

let package: Package = {
  Size: 0,
  DataType: "undefined",
  PackageIdentifier: "undefined"
};

function processPackage(package: Package) {
  console.log(package.Size);
  console.log(package.DataType);
  console.log(package.PackageIdentifier);
}

processPackage({
  Size: 32,
  DataType: "Byte",
  PackageIdentifier: "0x00"
});

processPackage(package);
