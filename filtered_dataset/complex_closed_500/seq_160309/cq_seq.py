import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04348, 0.04593).lineTo(-0.04508, 0.04593).lineTo(-0.04508, 0.0442).lineTo(-0.04348, 0.0442).lineTo(-0.04348, 0.04593).close()
solid=wp_sketch0.add(loop0).extrude(-0.0030783040807281707)
