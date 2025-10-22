import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-5.5626, 4.80695).lineTo(-5.4229, 4.80695).lineTo(-5.4229, 2.50825).lineTo(-5.5626, 2.50825).lineTo(-5.5626, 4.80695).close()
solid=wp_sketch0.add(loop0).extrude(-4.09589796255091)
