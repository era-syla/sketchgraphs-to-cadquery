import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.021, -0.045).lineTo(-0.021, -0.045).lineTo(-0.021, 0.045).lineTo(0.021, 0.045).lineTo(0.021, -0.045).close()
solid=wp_sketch0.add(loop0).extrude(-0.022481918261508867)
