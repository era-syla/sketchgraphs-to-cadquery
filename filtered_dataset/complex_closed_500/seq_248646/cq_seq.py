import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02754, 0.06178).threePointArc((0.02265, 0.0678), (0.01776, 0.06178)).lineTo(0.01996, 0.05124).threePointArc((0.02265, 0.04905), (0.02534, 0.05124)).lineTo(0.02754, 0.06178).close()
solid=wp_sketch0.add(loop0).extrude(0.02359692124497269)
