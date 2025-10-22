import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05835, -0.0781).lineTo(-0.14555, -0.0781).lineTo(-0.14555, -0.12477).lineTo(-0.05835, -0.12477).lineTo(-0.05835, -0.0781).close()
solid=wp_sketch0.add(loop0).extrude(-0.09993984703998787)
