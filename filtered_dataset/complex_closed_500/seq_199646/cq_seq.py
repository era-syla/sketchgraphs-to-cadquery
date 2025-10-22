import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02351, -0.03414).lineTo(0.03258, -0.03414).lineTo(0.03258, 0.02222).lineTo(-0.02351, 0.02222).lineTo(-0.02351, -0.03414).close()
solid=wp_sketch0.add(loop0).extrude(0.15608107979655123)
