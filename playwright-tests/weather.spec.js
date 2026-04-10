const { test, expect } = require('@playwright/test');

test('user can search city weather and see results', async ({ page }) => {
  await page.goto('http://127.0.0.1:8000/');

  await page.fill('input[name="city"]', 'Toronto');
  await page.click('button[type="submit"]');

  await page.waitForLoadState('networkidle');

  await expect(page.locator('h2')).toContainText('Toronto');
  await expect(page.locator('body')).toContainText('Summary:');
  await expect(page.locator('body')).toContainText('Recommendation:');
  await expect(page.locator('body')).toContainText('Risks:');
});