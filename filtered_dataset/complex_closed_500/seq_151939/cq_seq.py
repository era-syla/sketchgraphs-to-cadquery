import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.3095, 0.144).lineTo(0.3095, 0.144).lineTo(0.3095, -0.144).lineTo(-0.3095, -0.144).lineTo(-0.3095, 0.144).close()
solid=wp_sketch0.add(loop0).extrude(1.5863520178326733)
