/**
 * @jest-environment jsdom
 */
const { setTimeout } = require("../setTimeout");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("base.html", "htf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

describe("setTimeout function contains correct keys", () => {
    test("messages alert exist", () => {
        expect("alert" in setTimeout).toBe(true);
    });
});
