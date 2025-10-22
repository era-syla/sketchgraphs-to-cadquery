import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.01).lineTo(-0.04, 0.01).lineTo(-0.04, 0.02).lineTo(0.0, 0.02).lineTo(0.0, 0.14).lineTo(0.02494, 0.14).lineTo(0.1, 0.01).lineTo(0.1, -0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.24741239722123154)
