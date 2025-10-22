import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.6233, 1.7427).lineTo(1.3767, 1.7427).lineTo(1.3767, 1.1427).lineTo(-0.6233, 1.1427).lineTo(-0.6233, 1.7427).close()
solid=wp_sketch0.add(loop0).extrude(5.358978525571207)
