import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07, 0.04).lineTo(0.07, 0.01).lineTo(0.07, 0.04).lineTo(-0.07, 0.04).close()
solid=wp_sketch0.add(loop0).extrude(-0.06716565962615721)
