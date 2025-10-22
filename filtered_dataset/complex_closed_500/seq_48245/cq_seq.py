import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.03, 0.045).lineTo(0.03, -0.055).lineTo(-0.0291, -0.055).lineTo(-0.0291, -0.07).lineTo(-0.044, -0.07).lineTo(-0.044, 0.045).lineTo(0.03, 0.045).close()
solid=wp_sketch0.add(loop0).extrude(0.2820339526900828)
