/**
 * @jest-environment jsdom
 */
const { setTimeout } = require("../setTimeout");

describe("setTimeout function contains correct keys", () => {
    test("messages alert exist", () => {
        expect("alert" in setTimeout).toBe(false);
    });
});
