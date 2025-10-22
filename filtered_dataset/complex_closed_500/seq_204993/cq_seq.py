import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-1.4, 6.2).lineTo(1.3, 4.2).lineTo(-1.4, 4.2).lineTo(-1.4, 6.2).close()
solid=wp_sketch0.add(loop0).extrude(-4.780182284048178)
