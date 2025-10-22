import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, -0.0107).lineTo(0.0025, -0.0137).lineTo(0.0025, -0.0177).lineTo(-0.0025, -0.0177).lineTo(-0.0025, -0.0137).lineTo(0.0, -0.0107).close()
solid=wp_sketch0.add(loop0).extrude(0.01872701141265586)
