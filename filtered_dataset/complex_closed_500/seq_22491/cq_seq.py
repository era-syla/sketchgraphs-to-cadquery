import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.055, 0.06).lineTo(-0.055, 0.06).threePointArc((-0.05854, 0.05854), (-0.06, 0.055)).lineTo(-0.06, -0.055).threePointArc((-0.05854, -0.05854), (-0.055, -0.06)).lineTo(0.055, -0.06).threePointArc((0.05854, -0.05854), (0.06, -0.055)).lineTo(0.06, 0.055).threePointArc((0.05854, 0.05854), (0.055, 0.06)).close()
solid=wp_sketch0.add(loop0).extrude(0.093918025325052)
