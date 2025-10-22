import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.5, 0.0).threePointArc((0.25, 0.134), (0.0, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(1.3410734721536608)
