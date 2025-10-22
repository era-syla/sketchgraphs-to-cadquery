import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.2725, -0.8).lineTo(-0.1475, -0.8).lineTo(-0.1475, 0.142).lineTo(-0.2725, 0.142).lineTo(-0.2725, -0.8).close()
solid=wp_sketch0.add(loop0).extrude(1.1308535634291257)
