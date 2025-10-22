import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(5e-05, 0.03002).lineTo(0.01153, 0.02727).lineTo(0.00995, 0.02071).lineTo(-0.00152, 0.02347).lineTo(5e-05, 0.03002).close()
solid=wp_sketch0.add(loop0).extrude(0.004224489913631512)
