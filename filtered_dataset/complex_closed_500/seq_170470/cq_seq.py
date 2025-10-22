import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-5.5626, 7.1374).lineTo(-5.4229, 7.1374).lineTo(-5.4229, 4.94665).lineTo(-5.5626, 4.94665).lineTo(-5.5626, 7.1374).close()
solid=wp_sketch0.add(loop0).extrude(-2.080047391194865)
