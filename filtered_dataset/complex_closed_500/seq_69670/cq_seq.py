import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04, -0.26).lineTo(0.55, -0.26).lineTo(0.55, 0.26).lineTo(-0.04, 0.26).lineTo(-0.04, -0.26).close()
solid=wp_sketch0.add(loop0).extrude(1.7599979825992758)
