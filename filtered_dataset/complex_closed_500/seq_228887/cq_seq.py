import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03027, 0.02858).lineTo(-0.01122, 0.02858).lineTo(-0.01122, 0.02344).lineTo(-0.03027, 0.02344).lineTo(-0.03027, 0.02858).close()
solid=wp_sketch0.add(loop0).extrude(0.0062880024416523085)
