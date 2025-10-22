import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.055, 0.043).lineTo(-0.055, 0.043).threePointArc((-0.05712, 0.04212), (-0.058, 0.04)).lineTo(-0.058, -0.04).threePointArc((-0.05712, -0.04212), (-0.055, -0.043)).lineTo(0.055, -0.043).threePointArc((0.05712, -0.04212), (0.058, -0.04)).lineTo(0.058, 0.04).threePointArc((0.05712, 0.04212), (0.055, 0.043)).close()
solid=wp_sketch0.add(loop0).extrude(0.287136283381314)
