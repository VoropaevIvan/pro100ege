import NotFound from "./components/Pages/NotFound";
import Test from "./components/Pages/Test";
import Variants from "./components/Pages/Variants";

export const publicRoutes = [
  { path: "test", Component: Test },
  { path: "*", Component: NotFound },
  { path: "variants", Component: Variants },
];

export const authRoutes = [];

export const adminRoutes = [];
