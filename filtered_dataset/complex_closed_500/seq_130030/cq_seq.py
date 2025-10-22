import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0755, 0.0475).lineTo(0.0755, 0.0475).threePointArc((0.07904, 0.04604), (0.0805, 0.0425)).lineTo(0.0805, -0.0425).threePointArc((0.07904, -0.04604), (0.0755, -0.0475)).lineTo(-0.0755, -0.0475).threePointArc((-0.07904, -0.04604), (-0.0805, -0.0425)).lineTo(-0.0805, 0.0425).threePointArc((-0.07904, 0.04604), (-0.0755, 0.0475)).close()
solid=wp_sketch0.add(loop0).extrude(0.32307853369510237)
