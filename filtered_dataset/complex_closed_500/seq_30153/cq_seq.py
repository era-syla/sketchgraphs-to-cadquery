import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.1065, 0.0315).lineTo(-0.0815, 0.0315).lineTo(-0.0815, -0.0315).lineTo(-0.1065, -0.0315).lineTo(-0.1065, 0.0315).close()
solid=wp_sketch0.add(loop0).extrude(-0.11289782284227222)
