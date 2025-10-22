import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00035, 0.005).lineTo(0.00035, 0.005).threePointArc((0.00046, 0.00496), (0.0005, 0.00485)).lineTo(0.0005, 0.00265).threePointArc((0.00046, 0.00254), (0.00035, 0.0025)).lineTo(-0.00035, 0.0025).threePointArc((-0.00046, 0.00254), (-0.0005, 0.00265)).lineTo(-0.0005, 0.00485).threePointArc((-0.00046, 0.00496), (-0.00035, 0.005)).close()
solid=wp_sketch0.add(loop0).extrude(-0.00613764219982261)
