import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0254, 0.0127).lineTo(0.0254, 0.0127).threePointArc((0.02989, 0.01084), (0.03175, 0.00635)).lineTo(0.03175, -0.00635).threePointArc((0.02989, -0.01084), (0.0254, -0.0127)).lineTo(-0.0254, -0.0127).threePointArc((-0.02989, -0.01084), (-0.03175, -0.00635)).lineTo(-0.03175, 0.00635).threePointArc((-0.02989, 0.01084), (-0.0254, 0.0127)).close()
solid=wp_sketch0.add(loop0).extrude(0.1706486155548448)
