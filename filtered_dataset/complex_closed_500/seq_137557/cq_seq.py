import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.04502).lineTo(0.00354, 0.04149).lineTo(-0.0, 0.03795).lineTo(-0.00354, 0.04149).lineTo(-0.0, 0.04502).close()
solid=wp_sketch0.add(loop0).extrude(0.01890550848370113)
