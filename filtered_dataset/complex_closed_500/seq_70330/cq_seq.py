import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.236, -0.01908).lineTo(-0.224, -0.01908).lineTo(-0.224, -0.02508).lineTo(-0.236, -0.02508).lineTo(-0.236, -0.01908).close()
solid=wp_sketch0.add(loop0).extrude(0.025903864740976987)
