import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.00833).lineTo(0.00486, -0.00833).lineTo(0.00486, 0.01312).lineTo(0.0, 0.01312).lineTo(0.0, -0.00833).close()
solid=wp_sketch0.add(loop0).extrude(0.03061853098573376)
