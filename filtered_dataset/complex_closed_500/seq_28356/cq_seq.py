import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.08191, 0.08956).lineTo(0.15105, 0.08956).lineTo(0.15105, 0.07789).lineTo(-0.08191, 0.07789).lineTo(-0.08191, 0.08956).close()
solid=wp_sketch0.add(loop0).extrude(-0.2604964119472989)
