import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0125, 0.0).lineTo(-0.0125, 0.03).lineTo(-0.0255, 0.03).lineTo(-0.0255, 0.02625).lineTo(-0.0315, 0.02625).lineTo(-0.0315, 0.03).lineTo(-0.0335, 0.03).lineTo(-0.0335, 0.02).lineTo(-0.023, 0.02).lineTo(-0.023, 0.0).lineTo(-0.0125, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.0010464857281209427)
