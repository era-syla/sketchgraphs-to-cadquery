import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.22543, -0.04445).lineTo(-0.20638, -0.04445).lineTo(-0.20638, 0.04445).lineTo(-0.22543, 0.04445).lineTo(-0.22543, -0.04445).close()
solid=wp_sketch0.add(loop0).extrude(0.07118749114966104)
