import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00348, -0.00451).lineTo(-0.00648, -0.00451).lineTo(-0.00648, -0.02199).lineTo(-0.00348, -0.02199).lineTo(-0.00348, -0.00451).close()
solid=wp_sketch0.add(loop0).extrude(0.05229679335213747)
