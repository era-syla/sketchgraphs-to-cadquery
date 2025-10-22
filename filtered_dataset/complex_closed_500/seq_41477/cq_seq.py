import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-2.775, 0.43).lineTo(-2.025, 0.43).lineTo(-2.025, 0.4).lineTo(-2.775, 0.4).lineTo(-2.775, 0.43).close()
solid=wp_sketch0.add(loop0).extrude(0.6972201194732945)
