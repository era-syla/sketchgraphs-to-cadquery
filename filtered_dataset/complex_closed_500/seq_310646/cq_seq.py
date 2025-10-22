import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03841, 0.00159).lineTo(0.03841, 0.00159).lineTo(0.03841, 0.05341).lineTo(-0.03841, 0.05341).lineTo(-0.03841, 0.00159).close()
solid=wp_sketch0.add(loop0).extrude(0.05488514010504768)
