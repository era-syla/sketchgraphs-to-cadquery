import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.006, 0.0026).lineTo(0.005, 0.0026).lineTo(0.005, 0.0015).lineTo(-0.006, 0.0015).lineTo(-0.006, 0.0026).close()
solid=wp_sketch0.add(loop0).extrude(0.013662213859982533)
