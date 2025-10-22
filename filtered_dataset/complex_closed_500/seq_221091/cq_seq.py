import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-6.096, 4.572).lineTo(-0.0, 4.572).lineTo(-0.0, 0.0).lineTo(-6.096, 0.0).lineTo(-6.096, 4.572).close()
solid=wp_sketch0.add(loop0).extrude(18.014158539623388)
