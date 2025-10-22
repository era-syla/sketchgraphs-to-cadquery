import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.375, 0.08).lineTo(-0.225, 0.08).lineTo(-0.225, 0.42).lineTo(-0.375, 0.42).lineTo(-0.375, 0.08).close()
solid=wp_sketch0.add(loop0).extrude(0.8796628778511905)
