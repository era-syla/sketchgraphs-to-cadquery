import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1016, 0.04445).lineTo(-0.1016, 0.04445).lineTo(-0.1016, -0.04445).lineTo(0.1016, -0.04445).lineTo(0.1016, 0.04445).close()
solid=wp_sketch0.add(loop0).extrude(0.6095705567991438)
