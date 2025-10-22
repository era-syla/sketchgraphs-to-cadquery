import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0054, 0.028).lineTo(-0.0086, 0.028).threePointArc((-0.01072, 0.02712), (-0.0116, 0.025)).lineTo(-0.0116, 0.0067).threePointArc((-0.01072, 0.00458), (-0.0086, 0.0037)).lineTo(0.0054, 0.0037).threePointArc((0.00752, 0.00458), (0.0084, 0.0067)).lineTo(0.0084, 0.025).threePointArc((0.00752, 0.02712), (0.0054, 0.028)).close()
solid=wp_sketch0.add(loop0).extrude(0.011572136326725671)
