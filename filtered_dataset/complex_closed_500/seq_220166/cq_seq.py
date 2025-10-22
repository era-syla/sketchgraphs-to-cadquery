import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.045, 0.045).lineTo(-0.045, 0.045).lineTo(-0.045, -0.045).lineTo(0.045, -0.045).lineTo(0.045, 0.045).close()
solid=wp_sketch0.add(loop0).extrude(0.21390285786680666)
