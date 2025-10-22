import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.61053, 0.7692).lineTo(0.60867, 0.7692).lineTo(0.60867, -0.2976).lineTo(-0.61053, -0.2976).lineTo(-0.61053, 0.7692).close()
solid=wp_sketch0.add(loop0).extrude(0.17416875253245365)
