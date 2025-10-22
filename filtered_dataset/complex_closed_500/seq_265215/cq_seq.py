import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.0254).threePointArc((0.00225, 0.02447), (0.00317, 0.02223)).lineTo(0.00318, 0.00317).lineTo(0.02223, 0.00317).threePointArc((0.02447, 0.00225), (0.0254, 0.0)).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.009639117653629436)
