import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.05058, 0.0762).lineTo(0.05058, 0.08075).lineTo(0.04601, 0.07847).lineTo(0.05058, 0.0762).close()
solid=wp_sketch0.add(loop0).extrude(0.0016010418976694272)
