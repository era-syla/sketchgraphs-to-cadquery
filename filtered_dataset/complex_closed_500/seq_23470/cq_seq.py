import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0254, 0.0254).threePointArc((0.01524, 0.03556), (0.00508, 0.0254)).lineTo(0.0254, 0.0254).close()
solid=wp_sketch0.add(loop0).extrude(0.02092112879118839)
